<template>
  <div>
    <Header />
    <div class="container-md mt-5">
      <h1>EDIT CATEGORY</h1>
      <form>
        <!-- Category input -->
        <div class="form-outline mb-4">
          <label class="form-label" for="form6Example7">Choice Category</label>
          <select
            class="form-select"
            aria-label="Default select example"
            v-model="data.id"
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

        <!-- name category -->
        <div class="form-outline mb-4">
          <label class="form-label">Rename Category</label>
          <div class="input-group mb-4">
            <input type="text" class="form-control" v-model="data.name" />
          </div>
        </div>

        <!-- Submit button -->
        <router-link to="/">
          <button
            @click="submitEditCategory"
            class="btn btn-primary btn-block mb-4"
          >
            Edit Category
          </button>
        </router-link>

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
  name: "EditCategory",
  components: { Header },
  data() {
    return {
      data: {
        id: "",
        name: "",
      },
    };
  },
  methods: {
    getCategoryIdByCategory(name) {
      return this.$store.state.categories.find((x) => x.name === name).id;
    },
    submitEditCategory() {
      const res = axios
        .post(
          "https://laptrinhcautrucapi.herokuapp.com/category/edit_category",
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