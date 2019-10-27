from django.shortcuts import render, redirect
from ecom_app.lib.tb_admin import tb_admin
from ecom_app.lib.tb_user import tb_user
from ecom_app.lib.tb_category import tb_category
from ecom_app.lib.tb_product import tb_product

# Create your views here.

def touserhome(request):
    if request.method == 'GET':
        if 'useradmin' in request.COOKIES:
            return redirect(userhome)
        return render(request, 'login.html', {})
    if request.method == 'POST':
        user = request.POST['email']
        password = request.POST['password']
        admin = tb_admin()
        admin.connectToDB('localhost', 'root', '')
        if admin.authenticate(user, password):
            admin.closeConnection()
            response = redirect(userhome)
            response.set_cookie('useradmin', user)
            return response
        else:
            admin.closeConnection()
            return redirect(touserhome)

def signout(request):
    response = redirect(touserhome)
    response.delete_cookie('useradmin')
    return response

def userhome(request):
    if 'useradmin' in request.COOKIES:
        user = tb_user()
        user.connectToDB('localhost', 'root', '')
        if request.method == "POST":
            if request.POST['operation'] == 'delete':
                user.deleteUser(request.POST['delThis'])
                user.closeConnection()
                return redirect(userhome)
        users = user.getAllData()
        user.closeConnection()
        return render(request, 'user/home.html', {'users':users, 'total':len(users)})
    else:
        return redirect(touserhome)

def edituser(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            users = user.getData(user_id)
            user.closeConnection()
            return render(request, 'user/edit.html', {'users': users})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editeduser(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST':
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            user_id = request.POST['id']
            user_name = request.POST['uname']
            gender = request.POST['gender']
            email = request.POST['email']
            mobile = request.POST['mobile']
            password = request.POST['password']
            address = request.POST['address']
            filePath = "/user/{}.jpg".format(user_name)
            from os import rename
            rename("ecom_app/static/images/user/{}.jpg".format(user.getData(user_id)[1]), "ecom_app/static/images{}".format(filePath))
            user.editUserWithPhoto(user_id, user_name, gender, email, mobile, password, address, filePath)
            try:
                photo = request.FILES['photo']
                f = open("ecom_app/static/images/user/{}.jpg".format(user_name), 'wb')
                for i in photo:
                    f.write(i)
                f.close()
            except:
                pass
            user.closeConnection()
            return redirect(userhome)
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def insertnewuser(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'user/insert.html', {})
    else:
        return redirect(touserhome)

def insertednewuser(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        user = tb_user()
        user.connectToDB('localhost', 'root', '')
        uname = request.POST['uname']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        address = request.POST['address']
        imgData = request.FILES['photo']
        # imgData = imgData.read().decode()
        filePath = "/user/{}.jpg".format(uname)
        f = open("ecom_app/static/images{}".format(filePath), 'wb')
        for i in imgData:
            f.write(i)
        f.close()
        # sourceEncoding = "ISO-8859-1"
        # targetEncoding = "utf-8"
        # source = open("ecom_app/static/temp/0.jpg")
        # target = open("ecom_app/static/temp/0.jpg", "w")
        # target.write(source.read())
        # source.close()
        # target.close()
        # f = open("ecom_app/static/temp/0.jpg", 'rb')
        # imgData = f.read().decode()
        # f.close()
        user.insertUser(uname, gender, email, mobile, password, address, filePath)
        user.closeConnection()
        return redirect(userhome)
    else:
        return redirect(touserhome)

def useractive(request):
    if 'useradmin' in request.COOKIES:
        stuObj = tb_user()
        stuObj.connectToDB('localhost', 'root', '')
        ID = request.GET['activeThis']
        status = request.GET['toggle1']
        stuObj.updateActive(ID, status)
        stuObj.closeConnection()
        return redirect(userhome)
    else:
        return redirect(touserhome)

def producthome(request):
    if 'useradmin' in request.COOKIES:
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        if request.method == "POST":
            if request.POST['operation'] == 'delete':
                product.deleteProduct(request.POST['delThis'])
                product.closeConnection()
                return redirect(producthome)
        products = product.getAllData()
        product.closeConnection()
        return render(request, 'product/home.html', {'products': products, 'total': len(products)})
    else:
        return redirect(touserhome)

def productactive(request):
    if 'useradmin' in request.COOKIES:
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        ID = request.GET['activeThis']
        status = request.GET['toggle1']
        product.updateActive(ID, status)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def insertnewproduct(request):
    if 'useradmin' in request.COOKIES:
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        categories = category.getAllCategoryNames()
        category.closeConnection()
        return render(request, 'product/insert.html', {'categories': categories})
    else:
        return redirect(touserhome)

def insertednewproduct(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        pname = request.POST['pname']
        pdetails = request.POST['pdetails']
        pprice = request.POST['pprice']
        photo = request.FILES['photo']
        category = request.POST['category']
        filePath = "/product/{}.jpg".format(pname)
        f = open("ecom_app/static/images{}".format(filePath), 'wb')
        for i in photo:
            f.write(i)
        f.close()
        product.insertProduct(pname, pdetails, pprice, filePath, category)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def editproduct(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            product = tb_product()
            product.connectToDB('localhost', 'root', '')
            products = product.getData(user_id)
            product.closeConnection()
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            categories = category.getAllCategoryNames()
            category.closeConnection()
            return render(request, 'product/edit.html', {'products': products, 'categories': categories})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedproduct(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        id = request.POST['id']
        pname = request.POST['pname']
        pdetails = request.POST['pdetails']
        pprice = request.POST['pprice']
        category = request.POST['category']
        filePath = "/product/{}.jpg".format(pname)
        try:
            photo = request.FILES['photo']
            f = open("ecom_app/static/images{}".format(filePath), 'wb')
            for i in photo:
                f.write(i)
            f.close()
        except:
            pass
        product.editProduct(pname, pdetails, pprice, filePath, category, id)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def categoryhome(request):
    if 'useradmin' in request.COOKIES:
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        if request.method == 'POST':
            if request.POST['operation'] == 'delete':
                cat_id = request.POST['delThis']
                category.deleteCategory(cat_id)
                category.closeConnection()
                return redirect(categoryhome)
        categories = category.getAllCategories()
        total = len(categories)
        category.closeConnection()
        return render(request, 'category/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)

def insertnewcategory(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'category/insert.html', {})
    else:
        return redirect(touserhome)

def insertednewcategory(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        cat = request.POST['category']
        category.insertCategory(cat)
        category.closeConnection()
        return redirect(categoryhome)
    else:
        return redirect(touserhome)

def editcategory(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            cat_id = request.POST['editThis']
            cat = category.getCategory(cat_id)
            category.closeConnection()
            return render(request, 'category/edit.html', {'cat': cat})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedcategory(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST':
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            cat_id = request.POST['id']
            cat_name = request.POST['category']
            category.editCategory(cat_id, cat_name)
            category.closeConnection()
            return redirect(categoryhome)
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def orderdetailshome(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'orderdetails/home.html', {})
    else:
        return redirect(touserhome)

def ordermasterhome(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'ordermaster/home.html', {})
    else:
        return redirect(touserhome)