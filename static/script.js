const products = [
  { id: 1, name: "Apples", price: 120, image: "https://www.shutterstock.com/image-photo/red-apple-cut-half-water-600nw-2532255795.jpg" },
  { id: 2, name: "Bananas", price: 60, image: "https://i.ndtvimg.com/i/2016-04/banana-625_625x350_41459935133.jpg" },
  { id: 3, name: "Tomatoes", price: 80, image: "https://cdn2.stylecraze.com/wp-content/uploads/2013/05/296-18-Amazing-Health-Benefits-Of-Tomatoes-497181099.jpg.webp" },
  { id: 4, name: "Carrots", price: 50, image: "https://www.trustbasket.com/cdn/shop/articles/Carrot.jpg?v=1688378789" },
  { id: 5, name: "Potatoes", price: 40, image: "https://rukminim2.flixcart.com/image/480/640/kshtxu80/vegetable/f/e/a/1-potato-local-unbranded-no-whole-original-imag6fmst7xhaza8.jpeg?q=90" },
  { id: 6, name: "Milk", price: 55, image: "https://askmilking.com/wp-content/uploads/2024/12/milk-5.png" },
  { id: 7, name: "Bread", price: 45, image: "https://www.bbassets.com/media/uploads/p/xl/40037465_1-fresho-white-big-bread-slices-safe-preservative-free.jpg" },
  { id: 8, name: "Eggs (6 pcs)", price: 70, image: "https://s.yimg.com/ny/api/res/1.2/qjiN6tqC7wMQeYAkx2vgsA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyNDI7aD04Mjg7Y2Y9d2VicA--/https://media.zenfs.com/en/parade_250/72cfbb2b67faf4e85a592367ac901428" },
  { id: 9, name: "Cheese", price: 110, image: "https://i.ytimg.com/vi/ptk5XtW4GMI/sddefault.jpg" },
  { id: 10, name: "Rice (1kg)", price: 90, image: "https://media.istockphoto.com/id/154135449/photo/white-uncooked-rice.jpg?s=612x612&w=0&k=20&c=Uk6T6tKFiEkAB33W7XjDzbVJUolBkY6wNX4vOkjEmXg=" },
  { id: 11, name: "Wheat Flour (1kg)", price: 65, image: "https://dhatuorganics.com/wp-content/uploads/2024/09/Stock-2-10.jpg" },
  { id: 12, name: "Sugar (1kg)", price: 45, image: "https://img.lb.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/article_thumbnails/other/spoonful_of_sugar_other/1800x1200_spoonful_of_sugar_other.jpg" },
  { id: 13, name: "Coffee", price: 150, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI6WpWtXVTvPyHyBeucN01Ei8yunfgUB6V7A&s" },
  { id: 14, name: "Tea Powder", price: 95, image: "https://www.shutterstock.com/image-photo/black-tea-powder-dry-dust-260nw-1209350329.jpg" },
  { id: 15, name: "Juice (1L)", price: 120, image: "https://c8.alamy.com/comp/MM5YT1/juice-smoothie-smoothies-in-bottle-square-fruit-fruits-isolated-on-a-white-background-MM5YT1.jpg" },
  { id: 16, name: "Onions (1kg)", price: 50, image: "https://cdn.shopify.com/s/files/1/0523/9934/1736/files/5-onion-un-branded-no-whole-original-imafdsyg4ykqcyt4.webp?v=1693460821" },
  { id: 17, name: "Spinach", price: 40, image: "https://www.mahagro.com/cdn/shop/articles/spinach.jpg?v=1490962590" },
  { id: 18, name: "Butter", price: 90, image: "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2024-07/healthiest-butter-jp-240709-8ce75e.jpg" },
  { id: 19, name: "Yogurt", price: 60, image: "https://img.freepik.com/free-vector/realistic-vector-icon-illustration-strawberry-yoghurt-jar-with-spoon-full-yogurt-isolated_134830-2521.jpg" },
  { id: 20, name: "Soft Drink (500ml)", price: 35, image: "https://static.wixstatic.com/media/8f1abd_80bf432a005041b59c2a7fa1960ce71e~mv2.jpeg/v1/fill/w_8499,h_3727,al_c,q_90/8f1abd_80bf432a005041b59c2a7fa1960ce71e~mv2.jpeg" },
  { id: 21, name: "Soap", price: 30, image: "https://www.southernliving.com/thmb/eVspV1hl3sWompTu1tZnm4ZWtuM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1264622523-a30616de131e4d4daffc77c8c7774a56.jpg" },
  { id: 22, name: "Toothpaste", price: 60, image: "https://www.adinath.co.in/wp-content/uploads/2023/04/Toothpaste-Manufacturing-Plant.jpg" },
  { id: 23, name: "Cooking Oil (1L)", price: 150, image: "https://connect.healthkart.com/wp-content/uploads/2016/08/banner-56.jpg" },
  { id: 24, name: "Salt (1kg)", price: 25, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpUhuwj6s0dUH05XODTEESS3eiYtsSptTCJA&s" },
  { id: 25, name: "Honey", price: 180, image: "https://m.media-amazon.com/images/I/61t3CUyXyeL.jpg" }
];

const productList = document.getElementById("product-list");
const cartItems = document.getElementById("cart-items");
const cartCount = document.getElementById("cart-total");
const cartTotal = document.getElementById("cart-total");

let cart = [];

function loadProducts() {
  productList.innerHTML = "";

  products.forEach(product => {
    const card = document.createElement("div");
    card.className = "bg-white shadow-lg rounded-xl p-4 text-center hover:shadow-2xl transition duration-300";
    card.innerHTML = `
      <img src="${product.image}" alt="${product.name}" class="w-24 h-24 object-cover rounded-md mx-auto mb-3">
      <h3 class="text-lg font-semibold text-green-700">${product.name}</h3>
      <p class="text-gray-600 mb-2">₹${product.price}</p>
      <button onclick="addToCart(${product.id})" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition">Add to Cart</button>
    `;
    productList.appendChild(card);
  });
}

function addToCart(id) {
  const product = products.find(p => p.id === id);
  const existing = cart.find(item => item.id === id);
  if (existing) existing.quantity += 1;
  else cart.push({ ...product, quantity: 1 });
  updateCart();
}

function updateCart() {
  cartItems.innerHTML = "";
  let total = 0;
  cart.forEach(item => {
    const li = document.createElement("li");
    li.className = "flex justify-between";
    li.innerHTML = `<span>${item.name} x ${item.quantity}</span><span>₹${item.price * item.quantity}</span>`;
    cartItems.appendChild(li);
    total += item.price * item.quantity;
  });
  cartTotal.textContent = total;
}

loadProducts();
