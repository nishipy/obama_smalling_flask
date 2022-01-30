# Flask app for Obama or Smalling Prediction

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

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">お盆休みなのでflaskで遊んでる <a href="https://t.co/eVHuBMx8ZZ">pic.twitter.com/eVHuBMx8ZZ</a></p>&mdash; nishipy (@iamnishipy) <a href="https://twitter.com/iamnishipy/status/1161564025454379009?ref_src=twsrc%5Etfw">August 14, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Related blog post and tweet
- [FlaskとKerasでオバマとスモーリングを自動判別するWebアプリケーションを作る -前編-](https://nishipy.com/archives/1162)
- [お盆休みなのでflaskで遊んでる](https://twitter.com/i/status/1161564025454379009)
