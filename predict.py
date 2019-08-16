# coding: utf-8
# ref: https://flask.palletsprojects.com/en/master/patterns/fileuploads/
import os, sys
from flask import Flask, flash, request, redirect, url_for, render_template
# secure_filename: アップロードされたファイル名を確認し、危険なコマンドのような文字列が含まれていればエスケープ
from werkzeug.utils import secure_filename
from keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)
app.secret_key = 'secret_key'

# 定数は大文字で書くのが通例
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
model = load_model('obama_smalling_201908.h5')
graph = tf.get_default_graph()

app = Flask(__name__)
# Flaskアプリのconfigファイルに設定
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def is_allowed_file(filename):
    # splitやrsplitの2つめの引数
    # -> rsplit('.', 1): 1回だけ区切ってあとは繋げておく
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('predict'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # ファイルが指定されたか確認
        if 'file' not in request.files:
            flash('No file.')
            # ファイルがなければ、アップロードページに戻す
            return redirect(url_for('predict'))
        file = request.files['file']
        # ファイル名が空じゃないか確認
        if file.filename == '':
            flash('No file.')
            return redirect(url_for('predict'))
        if file and is_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            img = Image.open(filepath).convert('RGB')
            img = img.resize((150, 150))
            # 画像をnumpy.arrayに変更
            x = np.array(img, dtype=np.float32)
            x = x / 255.
            x = x.reshape((1,) + x.shape)
            
            global graph
            with graph.as_default():
                pred = model.predict(x, batch_size=1, verbose=0)
                score = np.max(pred)
                if(score >= 0.5):
                    person = 'Smalling'
                else:
                    person = 'Obama'
                    score = 1 - score

            resultmsg = '[{}] {:.4%} Sure.'.format(person, score)
            
            #session['resultmsg'] = resultmsg
            #session['filepath'] = filepath
            return render_template('result.html', resultmsg=resultmsg, filepath=filepath)

            # uploaded_file関数のページに転送される
            # return redirect(url_for('uploaded_file', filename=filename))
    # '''を入れると、複数行returnできる
    return render_template('predict.html')

#@app.route('result')
#def result():
#    if 'resultmsg' not in session:
#        return redirect(url_for('index'))
#    return render_template('result.html', resultmsg=session['resultmsg'], filepath=session['filepath'])

#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
#    # アップロードされたファイルを拾ってきて表示する
#    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)