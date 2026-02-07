from flask import Flask, jsonify, request

app= Flask(__name__)

books- [

    {
        "id": 1,
        "title": "Harry Potter i kamien filozoficzny",
        "autor": "J.K Tolkien",
        "year": 2001,
        "pages": 328

    },
    {
        "id": 2,
        "title": "Władca Pierścieni",
        "autor": "J.R.R Tolkien",
        "year": 1955,
        "pages": 586
    }

]

def sort_books_by_pages():
    return sorted(books, key=lambda book: book["pages"])
@app.route("/books", methods=["POST"])
def get_book():
    data = request_json  
    new_book = {
        "id": get_new_id(),
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "pages": data["pages"]
    }

    books.append(new_book)
    return jsonify(new_book), 201


if __name__ == "__main__":
    app.run(debug=True)