# 定義一個空字典來儲存圖書信息
library = {}

def add_book():
    book_info = input("Enter the title, genre, and price of the book (seperated by |): ")
    title, genre, price = book_info.split('|')
    title = title.strip()  # 去除標題前後的空白
    genre = genre.strip()  # 去除類別前後的空白
    price = float(price.strip())  # 去除價格前後的空白並轉換為浮點數
    library[title] = (genre, price)  # 將書籍信息添加到字典中
    print(f"The book '{title}' has been added.")  # 打印添加成功消息
    return True

def remove_book():
    title = input("Enter the title of the book you want to remove: ").strip()  # 提示輸入標題並去除前後空白
    if title in library:
        del library[title]  # 刪除字典中的書籍
        print(f"The book '{title}' has been removed.")  # 打印刪除成功消息
        return True
    else:
        print(f"Error: The book '{title}' was not found in the library.")  # 打印錯誤消息
        return False

def get_book_info():
    title = input("Enter the title of the book: ").strip()  # 提示輸入標題並去除前後空白
    if title in library:
        genre, price = library[title]  # 獲取書籍的類別和價格
        print(f"Title: {title}, Genre: {genre}, Price: {price}")  # 打印書籍信息
    else:
        print(f"Error: The book '{title}' was not found in the library.")  # 打印錯誤消息

def list_books():
    if not library:
        print("\nThe library is empty.\n")  # 如果圖書字典為空，打印消息
        return False
    print()
    for title, (genre, price) in sorted(library.items()):  # 按照標題的字母順序列出書籍
        print("%s (%s, $%.2f)" % (title, genre, price))  # 打印書籍的標題、類別和價格
    print()
    return True

def list_books_by_genre():
    genre = input("Enter the genre to search for: ").strip()  # 提示輸入類別並去除前後空白
    found = False
    for title in sorted(library.keys()):  # 按照標題的字母順序遍歷書籍
        if library[title][0] == genre:
            print(f"Title: {title}, Price: {library[title][1]:.2f}")  # 打印書籍的標題和價格
            found = True
    if not found:
        print(f"No books found in the genre '{genre}'.")  # 如果未找到書籍，打印錯誤消息
        return False
    return True

# 主循環，用於顯示菜單並處理用戶選擇
while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")  # 提示輸入選擇
    if choice == "1":
        add_book_return = add_book()  # 添加書籍
        if add_book_return:
            list_books()  # 列出所有書籍
    elif choice == "2":
        remove_book_return = remove_book()  # 刪除書籍
        if remove_book_return:
            list_books()  # 列出所有書籍
    elif choice == "3":
        get_book_info()  # 查詢書籍信息
    elif choice == "4":
        list_books()  # 列出所有書籍
    elif choice == "5":
        list_books_by_genre()  # 按類別列出書籍
    elif choice == "6":
        break  # 退出循環
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")  # 錯誤輸入提示

print("Goodbye!")  # 打印再見消息

