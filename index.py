from flask  import Flask, request, json
from markupsafe import escape
from products import product_list, defProduct

print(product_list)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return 'Welcome to my API!'

@app.route("/products", methods=["GET"])
def getProducts():
    return product_list

@app.route('/getProduct/<string:product_name>', methods= ["GET"])
def getProduct(product_name):
    productFound = [product for product in product_list if product["name"]==product_name]
    print(productFound)
    return productFound[0]

@app.route('/createProduct', methods=["POST"])
def createProduct():
    data = json.loads(request.data)
    if list(data.keys()) == list(defProduct.keys()):
        product_list.append(data)
        return data
    else: 
        return 'invalid'
@app.route('/updateProduct/<string:product_name>', methods=["PUT"])
def editProduct(product_name):
    data = json.loads(request.data)
    product  = {
        "name": data["name"],
        "stock": data["stock"],
        "price": data["price"]
    }
        
    productFound = [product for product in product_list if product["name"]==product_name]
    try:
        productPos = product_list.index(productFound[0])
        product_list[productPos] = product
        return product_list[productPos]
    except:
        return 'Product not found!'

@app.route('/deleteProduct/<string:product_name>', methods=["DELETE"])
def removeProduct(product_name):

    productFound = [product for product in product_list if product["name"]==product_name]
    try:
        productPos = product_list.index(productFound[0])
        product_list.remove(product_list[productPos])
        return {
            "removed": product_list[productPos]
        }
    except Exception as e:
        print(e)
        return 'Product could not be eliminated'
    
