# BeautifulSoup - Web Crawling
## **1) Web Crawling**
- **Web crawling** là quá trình tự động trích xuất các thông tin từ các trang web và lưu trữ nó dưới một định dạng phù hợp . Chương trình mà thực hiện công việc này gọi là **web crawler** .
- Thông thường, khi muốn lấy một số thông tin từ các trang web , chúng ta sẽ dùng các **API** mà các trang đó cung cấp . Đây là cách đơn giản , tuy nhiên không phải trang web nào cũng cung cấp sẵn **API** cho chúng ta sử dụng . Do đó chúng ta cần một kĩ thuật để lấy các thông tin từ các trang web đó mà không thông qua **API** .
## **2) BeautifulSoup**
### **2.1) Giới thiệu**
- Thư viện **BeautifulSoup** là một thư viện của **Python** cho phép chúng ta lấy dữ liệu từ **HTML** đơn giản và hiệu quả .
- Phiên bản mới nhất : `4.8.1` ( **BeautifulSoup `4`** )
- Github : https://github.com/waylan/beautifulsoup
### **2.2) Cài đặt**
- **B1 :** Kiểm tra thư viện `bs4` đã được cài đặt chưa :
    ```
    $ python -c "import bs4; print(bs4.__version__);"
    ```
    => Output nếu chưa được cài đặt :
    ```py
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'bs4'
    ```
- **B2 :** Cài đặt `bs4` :
    ```
    $ sudo pip install beautifulsoup4
    ```