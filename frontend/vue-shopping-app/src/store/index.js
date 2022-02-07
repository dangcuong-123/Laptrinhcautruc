import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    products: [],
    categories: []
  },
  mutations: {
    getProducts(state, products){
      state.products = products
    },
    getCategory(state, categories) {
      state.categories = categories
    }
  },
  actions: {
    getProductsAction({commit}){
      axios('https://laptrinhcautrucapi.herokuapp.com/product/show').then(res => {
        commit('getProducts', res.data)
      })

    },
    getCategoriesAction({commit}){
      axios('https://laptrinhcautrucapi.herokuapp.com/category/show').then(res => {
        commit('getCategory', res.data)
      })

    }
  },
  modules: {
  }
})
