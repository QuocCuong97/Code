# BeautifulSoup - Web Crawling
## **1) Web Crawling**
- **Web crawling** là quá trình tự động trích xuất các thông tin từ các trang web và lưu trữ nó dưới một định dạng phù hợp . Chương trình mà thực hiện công việc này gọi là **web crawler** .
- Thông thường, khi muốn lấy một số thông tin từ các trang web , chúng ta sẽ dùng các **API** mà các trang đó cung cấp . Đây là cách đơn giản , tuy nhiên không phải trang web nào cũng cung cấp sẵn **API** cho chúng ta sử dụng . Do đó chúng ta cần một kĩ thuật để lấy các thông tin từ các trang web đó mà không thông qua **API** .
## **2) BeautifulSoup**
### **2.1) Giới thiệu**
- Thư viện **BeautifulSoup** là một thư viện của **Python** cho phép chúng ta lấy dữ liệu từ **HTML** đơn giản và hiệu quả .
- Phiên bản mới nhất : `4.8.1` ( **BeautifulSoup `4`** )
- Github : https://github.com/waylan/beautifulsoup
### **2.2) Cài đặt BeautifulSoup**
- **B1 :** Kiểm tra thư viện `bs4` đã được cài đặt chưa :
    ```
    $ python3 -c "import bs4; print(bs4.__version__);"
    ```
    => Output nếu chưa được cài đặt :
    ```py
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'bs4'
    ```
    => Output nếu đã được cài đặt :
    ```
    4.8.1
    ```
- **B2 :** Cài đặt `bs4` :
    ```
    $ sudo pip install beautifulsoup4
    ```
### **2.3) Cài đặt các và sử dụng các parser**
- **BeautifulSoup** hỗ trợ thư viện **HTML parser** mặc định của **Python** ( `html.parser` ) và một số thư viện của bên thứ ba ( `lxml` hoặc `html5lib` ) . 
- Cài đặt các parser :
    - **`HTML5lib`** :
        ```
        $ sudo pip install html5lib
        ```
    - **`LXML`** :
        ```
        $ sudo pip install lxml
        ```
- Sử dụng các parser :
    - **Python’s `html.parser`** :
        ```py
        BeautifulSoup(markup, "html.parser")
        ```
    - **`lxml`’s HTML parser** :
        ```py
        BeautifulSoup(markup, "lxml")
        ```
    - **`lxml`’s XML parser** :
        ```py
        BeautifulSoup(markup, "lxml-xml")
        ```
        hoặc
        ```py
        BeautifulSoup(markup, "xml")
        ```
    - **`html5lib`** :
        ```py
        BeautifulSoup(markup, "html5lib")
        ```
### **2.4) Các loại object của Beautiful Soup**
- **Beautiful Soup** sẽ chuyển đổi văn bản **HTML** sang **Python tree object** . Tuy nhiên , chỉ cần quan tâm 4 loại object là : `Tag` , `NavigableString` , `BeautifulSoup` và `Comment` .
- **VD :** File mẫu `test.html` :
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <link rel="stylesheet" href="css.css" type="text/css">
    </head>
    <body>
        <!-- Items list -->
        <div class="items-list">
            <div class="item pull-right">
                <p class="title">Item 001</p>
                <p class="price">Price: 01$</p>
                <p><a href="#">Buy</a></p>
            </div>
            <div class="item pull-right">
                <p class="title">Item 002</p>
                <p class="price">Price: 02$</p>
                <p><a href="#">Buy</a></p>
            </div>
            <div class="item pull-right">
                <p class="title">Item 003</p>
                <p class="price">Price: 03$</p>
                <p><a href="#">Buy</a></p>
            </div>
            <div class="item pull-right">
                <p class="title">Item 004</p>
                <p class="price">Price: 04$</p>
                <p><a href="#">Buy</a></p>
            </div>
            <div class="item pull-right">
                <p class="title">Item 005</p>
                <p class="price">Price: 05$</p>
                <p><a href="#">Buy</a></p>
            </div>
        </div>
        <!-- End of items list -->
    </body>
    </html>
#### **2.4.1) `Tag`**
- Là một HTML (XML) tag .
- Tìm một tag ( hàm `find()` ) :
    ```py
    from bs4 import BeautifulSoup

    html_dom = BeautifulSoup(open('test.html'), 'html5lib')
    title_tag = html_dom.find('title')
    print(title_tag)
    ```
    => Output :
    ```
    <title>Document</title>
    ```
- Thuộc tính `name` : lấy ra tên của tag :
    ```py
    print(title_tag.name)
    ```
    => Output :
    ```
    title
    ```
