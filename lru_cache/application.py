from flask import Flask, jsonify

from functools import lru_cache

app = Flask(__name__)


@app.route('/')
def main():
    store_to_cache()
    return jsonify({'message': 'Stored'})


@lru_cache(maxsize=2)
def store_to_cache():
    return {'this_goes_to_cache': 'and_this_too'}


@app.route('/get_cache_info')
def get_cache_info():
    cache_info = store_to_cache.cache_info()
    return jsonify({
        'Hits': cache_info.hits,
        'Misses': cache_info.misses,
        'Maxsize': cache_info.maxsize,
        'Currsize': cache_info.currsize
    })


@app.route('/clear_cache')
def clear_cache():
    store_to_cache.cache_clear()
    return jsonify({'message': 'Cache cleared'})


if __name__ == '__main__':
    app.run()
