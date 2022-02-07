<template>
    <div class="container-md my-5">
        <div class="row">
            <div class="col-xl-3 col-lg-3 col-md-4 col-sm-5">
                <!-- Filter by categories -->
                <select class="form-select py-2 shadow-sm text-capitalize mb-4" v-model="filterByCategory">
                    <option value="">All Categories</option>
                    <option :value="product" v-for="product in eliminateDuplicatedCategories($store.state.products)" :key="product">
                        {{product}}
                    </option>
                </select>
                <!-- Sort by prices -->
                <select class="form-select py-2 shadow-sm mb-4" v-model="sortByPrice" @change="sortProductsByPrice($store.state.products)">
                    <option value="" disabled>Sort By Price</option>
                    <option value="increasingOrder">Increasing Order</option>
                    <option value="decreasingOrder">Decreasing Order</option>
                </select>
               <!-- Search Products by price -->
                <div class="input-group mb-4 shadow-sm">
                    <span class="input-group-text bg-white" id="basic-addon1">
                        From Price
                    </span>
                    <input type="text" class="form-control py-2" placeholder="VND" aria-describedby="basic-addon1" v-model="fromPrice">
                </div>
                <div class="input-group mb-4 shadow-sm">
                    <span class="input-group-text bg-white" id="basic-addon1">
                        To Price
                    </span>
                    <input type="text" class="form-control py-2" placeholder="VND" aria-describedby="basic-addon1" v-model="toPrice">
                </div>
            </div>
            <div class="col-xl-9 col-lg-9 col-md-8 col-sm-7">
                <!-- Search Products -->
                <div class="input-group mb-4 shadow-sm">
                    <span class="input-group-text bg-white" id="basic-addon1">
                        <i class="fas fa-search"></i>
                    </span>
                    <input type="text" class="form-control py-2" placeholder="Search for a product..." aria-label="Username" aria-describedby="basic-addon1" v-model="searchProduct">
                </div>
                <!-- Display Products -->
                <div class="d-flex flex-wrap justify-content-sm-between justify-content-center">
                    <div class="card mb-4 shadow-sm" v-for="product in filterProducts" :key="product.id">
                        <div class="card-img">
                            <img :src="product.image" class="card-img-top img-fluid" :alt="product.name">
                        </div>
                        <div class="card-body d-flex flex-column justify-content-between">
                            <div>
                                <h4 class="card-title mb-3">{{formatProduct(product.name)}}</h4>
                                <p class="my-2">
                                    <span class="text-muted">Category: </span>
                                    <span class="text-capitalize">
                                        {{ getCategoryById(product.category_id) }}
                                    </span>
                                </p>
                                <p class="my-2">
                                    <span class="text-muted">Price: </span>
                                    <span class="text-capitalize">
                                        {{formatPrice(product.price)}} VND
                                    </span>
                                </p>
                            </div>
                            <div class="d-inline-block mt-4">
                                <router-link :to="'/product/' + product.id" class="text-decoration-none">
                                    <button class="btn btn-warning btn-sm w-100 d-flex align-items-center justify-content-center">
                                        More Info
                                        <i class="fas fa-angle-double-right mx-1"></i>
                                    </button>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Products',
    data(){
        return{
            searchProduct: '',
            filterByCategory: '',
            sortByPrice: '',
            sortByRating: '',
            fromPrice: "0",
            toPrice: "10000000"
        }
    },
    computed:{
        filterProducts(){
            return this.$store.state.products.filter(product => {
                return product.name.toLowerCase().includes(this.searchProduct.toLowerCase()) &&
                    this.capitalized(this.getCategoryById(product.category_id)).includes(this.capitalized(this.filterByCategory)) &&
                    this.filterPrice(product.price)
            })
        }
    },
    methods:{
        formatProduct(product){
            if(product.length > 15){
                return product.slice(0,15) + '...'
            }else{
                return product
            }
        },
        filterPrice(product){
            return  this.fromPrice <= product && product <= this.toPrice;
        },
        formatPrice(product){
            return product.toFixed(2)
        },
        getCategoryById(id) {
            return this.$store.state.categories.find(x => x.id === id).name
        },
        eliminateDuplicatedCategories(products){
            let arr = []
            products.forEach(product => {
                arr.push(this.getCategoryById(product.category_id))
            })
            return [...new Set(arr)];
        },
        capitalized(data){
            return data.toString().charAt(0).toUpperCase() + data.toString().slice(1)
        },
        sortProductsByPrice(products){
            this.sortByRating = ''
            if(this.sortByPrice == 'increasingOrder'){
                return products.sort((a, b) => a.price - b.price)
            }else if(this.sortByPrice == 'decreasingOrder'){
                return products.sort((a, b) => b.price - a.price)
            }
        }
    }
}
</script>

<style lang="scss" scoped>
    .card{
        width: 21.25rem;
        .card-img{
            height: 22.5rem;
            width: 100%;
            img{
                height: 100%;
                width: 100%;
                transform: scale(0.75);
            }
        }
    }
</style>