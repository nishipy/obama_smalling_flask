# Flask app for Obama or Smalling Prediction

This is a simple Flask application for Obama or Smalling Prediction.
For more detail, see the [obama_smalling_predictor](https://github.com/nishipy/obama_smalling_predictor) repo!

## Prerequiste
```
$ conda -V
conda 4.10.3
```

## Set up environment
Suggest using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to set up our environment.
```
$ conda create -n os-flask python=3.7.2
$ conda activate os-flask
$ pip install -r ./requirements.txt
```

## Run flask app
```shell
$ cd <THIS_REPO>/src/
$ export FLASK_APP=predict.py
$ flask run
```

Then you can see the app runnning on your [`localhost:5000/predict`](http://localhost:5000/predict)

## Demo

https://user-images.githubusercontent.com/41185206/151708123-6570335d-b979-43ba-89c6-0ea7e76503b8.mp4


## Related blog post and tweet
- [FlaskとKerasでオバマとスモーリングを自動判別するWebアプリケーションを作る -前編-](https://nishipy.com/archives/1162)
- [お盆休みなのでflaskで遊んでる](https://twitter.com/i/status/1161564025454379009)
