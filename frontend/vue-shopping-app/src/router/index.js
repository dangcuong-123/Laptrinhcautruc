import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ProductDetails from '../views/ProductDetails.vue'
import AddProduct from '../views/AddProduct.vue'
import AddCategory from '../views/AddCategory.vue'
import DeleteCategory from '../views/DeleteCategory.vue'
import EditCategory from '../views/EditCategory.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/product/:id',
    name: 'ProductDetails',
    component: ProductDetails
  },
  {
    path: '/addProduct',
    name: 'AddProduct',
    component: AddProduct
  },
  {
    path: '/addCategory',
    name: 'AddCategory',
    component: AddCategory
  },
  {
    path: '/deleteCategory',
    name: 'DeleteCategory',
    component: DeleteCategory
  },
  {
    path: '/editCategory',
    name: 'EditCategory',
    component: EditCategory
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
