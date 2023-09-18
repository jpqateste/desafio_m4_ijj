import requests


def getAllBooks():
  response = requests.get('http://apilivro.jogajuntoinstituto.org/books/')
  if response:
    books = response.json()
    print(books)
  else:
    return response.status_code


def getBookId(id):
  response = requests.get(
      f'http://apilivro.jogajuntoinstituto.org/books/{id}/')
  if response:
    book = response.json()
    print(book)
  else:
    return response.status_code


def postNewBook(titleBook, descBook, autBook, gendBook):
  
  json_book_data = {
    'title': titleBook,
    'description': descBook,
    'author': autBook,
    'gender': gendBook,
}
  
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'X-CSRFToken': '9OBXbphmTfGB8LuLWtfb0JqLVjxvpSWpF94dmklJiPoDH5AU1RGEdWMVqbLVmHo8',
}
  
  response = requests.post('http://apilivro.jogajuntoinstituto.org/books/', headers = headers, json = json_book_data)

  if response.status_code == 201:
    print('Livro cadastrado com sucesso!')
  else:
    print(response.status_code)