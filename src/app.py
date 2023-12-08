"""Main application package."""

from typing import Any, Dict, List, Tuple, TypedDict, Union

from flask import Flask, request

app = Flask(__name__)


class Store(TypedDict):
    """Store type."""

    name: str
    items: List[Dict[str, Any]]


store_1: Store = {
    'name': 'My Wonderful Store',
    'items': [{'name': 'Chair', 'price': 15.99}],
}
store_2: Store = {
    'name': 'Your Wonderful Store',
    'items': [{'name': 'Table', 'price': 59.99}],
}

stores: List[Store] = [store_1, store_2]


@app.get('/stores')
def get_stores() -> Dict[str, List[Store]]:
    """Get all stores."""
    return {'stores': stores}


@app.post('/stores')
def create_store() -> Tuple[Store, int]:
    """Create a new store."""
    request_data = request.get_json()
    new_store: Store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return new_store, 201


@app.post('/stores/<string:name>/item')
def create_item(
    name: str
) -> Union[Tuple[Dict[str, Any], int], Tuple[Dict[str, Any], int]]:
    """Create a new item in a store by name."""
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)
            return new_item, 201
    return {'message': 'store not found'}, 404


@app.get('/stores/<string:name>')
def get_store(
    name: str
) -> Union[Tuple[Store, int], Tuple[Dict[str, List[Store]], int]]:
    """Get a store by name."""
    for store in stores:
        if store['name'] == name:
            return store, 200
    return {'stores': stores}, 404


@app.get('/stores/<string:name>/items')
def get_item_in_store(name: str) -> Union[Tuple[Any, int], Tuple[Dict[str, Any], int]]:
    """Get all items in a store by name."""
    for store in stores:
        if store['name'] == name:
            return {'items': store['items']}, 200
    return {'stores': stores}, 404
