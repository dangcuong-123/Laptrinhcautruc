<template>
  <div>
    <Header />
    <div class="container-md mt-5">
      <h1>ADD PRODUCT</h1>
      <form>
        <!-- 2 column grid layout with text inputs for the name product and brand product -->
        <div class="row mb-4">
          <div class="col">
            <div class="form-outline">
              <label class="form-label" for="form6Example1">Name Product</label>
              <input
                type="text"
                id="form6Example1"
                class="form-control"
                v-model="data.name"
              />
            </div>
          </div>
          <div class="col">
            <div class="form-outline">
              <label class="form-label" for="form6Example2"
                >Brand Product</label
              >
              <input
                type="text"
                id="form6Example2"
                class="form-control"
                v-model="data.brand"
              />
            </div>
          </div>
        </div>

        <!-- 2 column grid layout with text inputs for the color product and size product -->
        <div class="row mb-4">
          <div class="col">
            <div class="form-outline">
              <label class="form-label" for="form6Example3"
                >Color Product</label
              >
              <input
                type="text"
                id="form6Example3"
                class="form-control"
                v-model="data.color"
              />
            </div>
          </div>
          <div class="col">
            <div class="form-outline">
              <label class="form-label" for="form6Example4">Size Product</label>
              <input
                type="text"
                id="form6Example4"
                class="form-control"
                v-model="data.size"
              />
            </div>
          </div>
        </div>

        <!-- price product -->
        <div class="form-outline mb-4">
          <label class="form-label">Price</label>
          <div class="input-group mb-4">
            <input type="text" class="form-control" v-model="data.price" />
            <span class="input-group-text">VND</span>
          </div>
        </div>

        <!-- quantity product -->
        <div class="form-outline mb-4">
          <label class="form-label">Quantity</label>
          <div class="input-group mb-4">
            <input type="text" class="form-control" v-model="data.quantity" />
            <span class="input-group-text">QUANTILY</span>
          </div>
        </div>

        <!-- Details input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="form6Example7">Details</label>
          <textarea
            class="form-control"
            id="form6Example7"
            rows="4"
            v-model="data.detail"
          ></textarea>
        </div>

        <!-- Category input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="form6Example7">Category</label>
          <select
            class="form-select"
            aria-label="Default select example"
            v-model="data.category_id"
          >
            <option
              :value="getCategoryIdByCategory(category.name)"
              v-for="category in $store.state.categories"
              :key="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>

        <div class="mb-4">
          <label for="formFile" class="form-label">Image Product</label>
          <input
            class="form-control"
            type="file"
            id="formFile"
            accept=".jpg,.gif,.png"
            @change="onFileChange"
          />
        </div>

        <!-- Submit button -->
        <button
          @click.prevent="submitAddProduct"
          class="btn btn-primary btn-block mb-4"
        >
          Add Product
        </button>

        <div class="btn mb-4">
          <router-link to="/" class="text-decoration-none">
            <a href="#" class="btn btn-warning d-flex align-items-center">
              <i class="fas fa-arrow-left mx-1"></i>
              Back to Main Page
            </a>
          </router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import axios from "axios";

export default {
  name: "AddProduct",
  components: { Header },
  data() {
    return {
      data: {
        image: null,
        category_id: "",
        detail: "",
        quantity: "",
        price: "",
        size: "",
        color: "",
        brand: "",
        name: "",
      },
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.data.image = URL.createObjectURL(file);
    },
    getCategoryIdByCategory(name) {
      return this.$store.state.categories.find((x) => x.name === name).id;
    },
    submitAddProduct() {
      const res = axios
        .put(
          "https://laptrinhcautrucapi.herokuapp.com/productV2/add_product",
          this.data
        )
        .then((res) => {
          alert(res.data);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>