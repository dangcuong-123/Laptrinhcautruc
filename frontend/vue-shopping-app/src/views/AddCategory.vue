<template>
  <div>
    <Header />
    <div class="container-md mt-5">
      <h1>ADD CATEGORY</h1>
      <form>
        <!-- name category -->
        <div class="form-outline mb-4">
          <label class="form-label">Category Name</label>
          <div class="input-group mb-4">
            <input type="text" class="form-control" v-model="data.name" />
          </div>
        </div>

        <!-- Submit button -->
        <router-link to="/">
          <button
            @click="submitAddCategory"
            class="btn btn-primary btn-block mb-4"
          >
            Add Category
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
  name: "AddCategory",
  components: { Header },
  data() {
    return {
      data: {
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
    submitAddCategory() {
      const res = axios
        .put(
          "https://laptrinhcautrucapi.herokuapp.com/category/add_category",
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