import lib_requests

def exibir_menu():
    print("      _                          _             _")
    print("     | |                        | |           | |")
    print("     | | ___   __ _  __ _       | |_   _ _ __ | |_ ___")
    print(" _   | |/ _ \ / _` |/ _` |  _   | | | | | '_ \| __/ _ |")
    print("| |__| | (_) | (_| | (_| | | |__| | |_| | | | | || (_)|")
    print(" \____/ \___/ \__, |\__,_|  \____/ \__,_|_| |_|\__\___/")
    print("               __/ |")
    print("              |___/")

    print(" _____                 ___         _")
    print("|_   _|__ __ _ _ __   | __|__ _ _ (_)_ __")
    print("  | |/ -_) _` | '  \  | _/ -_) ' \| \ \ /")
    print("  |_|\___\__,_|_|_|_| |_|\___|_||_|_/_\_")

    print("="*80)
                           

    print("Menu:")
    print("1. Cadastrar um novo Livro")
    print("2. Exibir o acervo (Todos os nossos Livros)")
    print("3. Pesquisar um Livro por ID (Digite o ID o Livro)")
    print("4. Sair")

def searchBookId():
  opt = input('Digite o ID so Livro: ')
  lib_requests.getBookId(opt)

def createNewBook():
   titleBook = input('Digite o titulo do Livro: ')
   descBook = input('Digite uma descrção do Livro: ')
   autBook = input('Digite o ID do autor do Livro: ')
   gendBook = input('Digite o ID gênero do Livro: ')
   
   lib_requests.postNewBook(titleBook, descBook, autBook, gendBook)

def main():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            createNewBook()
        elif opcao == "2":
            lib_requests.getAllBooks()
        elif opcao == "3":
            
            searchBookId()

        elif opcao == "4":
            break
        else:
            print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    main()