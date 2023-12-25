## Uranus
## Step 0: Yêu cầu
```sh
python version 3.11.4
```
## Step 1: Install library
```sh
pip install -r requirements.txt
```

## Step 2: Migration Database
```sh
alembic upgrade head
```
```sh
alembic downgrade base
```

## Other: Update resource
```sh
pyrcc5 ui/resource.qrc -o ui/resource_rc.py
```

## Other: Update ui
```sh
pyuic5 ui/admin/home.ui -o src/views/ui_generated/admin/home.py

pyuic5 ui/admin/product_detail.ui -o src/views/ui_generated/admin/product_detail.py

pyuic5 ui/admin/order_detail.ui -o src/views/ui_generated/admin/order_detail.py

pyuic5 ui/admin/member_rank_detail.ui -o src/views/ui_generated/admin/member_rank_detail.py

pyuic5 ui/admin/customer_detail.ui -o src/views/ui_generated/admin/customer_detail.py  

pyuic5 ui/admin/supplier_detail.ui -o src/views/ui_generated/admin/supplier_detail.py 
 
pyuic5 ui/admin/import_detail.ui -o src/views/ui_generated/admin/import_detail.py
```



## Other: Lưu thay đổi của database
```sh
alembic revision --autogenerate -m "first commit"

```