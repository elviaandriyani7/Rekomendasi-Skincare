from flask import Flask, render_template, request

app = Flask(__name__)

# Data produk skincare
products = [
    {
        "name": "Vitamin C Serum",
        "type": "Serum",
        "skin_type": "kulit kusam",
        "ingredients": "Vitamin C, Hyaluronic Acid",
        "description": "Serum yang membantu mencerahkan dan melembapkan kulit.",
        "image_url": "images/vitaminC.jpg"
    },
    {
        "name": "Exfoliating Scrub",
        "type": "Scrub",
        "skin_type": "kulit kusam",
        "ingredients": "Sugar, Coconut Oil",
        "description": "Scrub lembut yang membantu mengangkat sel kulit mati.",
        "image_url": "images/Sugar.jpg"
    },
    {
        "name": "Brightening Moisturizer",
        "type": "Moisturizer",
        "skin_type": "kulit kusam",
        "ingredients": "Niacinamide, Vitamin E",
        "description": "Pelembap yang membantu mencerahkan dan melembapkan kulit.",
        "image_url": "images/Niacinamide.jpg"
    },
    {
        "name": "Oil Control Gel",
        "type": "Gel",
        "skin_type": "kulit berminyak",
        "ingredients": "Tea Tree Oil, Salicylic Acid",
        "description": "Gel yang membantu mengontrol minyak dan mencegah jerawat.",
        "image_url": "images/gelTeaTreeOil.jpg"
    },
    {
        "name": "Hydrating Moisturizer",
        "type": "Moisturizer",
        "skin_type": "kulit kering",
        "ingredients": "Hyaluronic Acid, Shea Butter",
        "description": "Pelembap yang memberikan hidrasi intensif untuk kulit kering.",
        "image_url": "images/Hyaluronic-Acid-Moisturizer-AM-.jpg"
    },
    {
        "name": "Acne Treatment Cream",
        "type": "Cream",
        "skin_type": "kulit berjerawat",
        "ingredients": "Benzoyl Peroxide, Salicylic Acid",
        "description": "Krim perawatan yang membantu mengurangi jerawat dan peradangan.",
        "image_url": "images/BenzoylPeroxideacne.jpg"
    },
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        complaint = request.form.get('complaint', '').lower()
        keywords = complaint.split(',')

        filtered_products = [
            product for product in products if any(keyword.strip() in product['skin_type'].lower() for keyword in keywords)
        ]
        
        return render_template('index.html', recommendations=filtered_products)
    
    return render_template('index.html', recommendations=[])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
