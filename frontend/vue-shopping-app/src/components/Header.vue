<template>
  <header class="py-3">
    <div class="container-md d-flex justify-content-between align-items-center">
      <h2 class="text-white">Vue Shopping</h2>
      <div class="d-flex flex-row-reverse">
        <div class="text-decoration-none p-2"> 
          <button v-if="$store.state.isAdmin" @click.prevent="$store.state.isAdmin=!$store.state.isAdmin"
            class="
              btn btn-d btn-sm
              w-100
              d-flex
              align-items-center
              justify-content-center
              btn-success
            "
          >
            Admin
          </button>
          <button v-if="!$store.state.isAdmin" @click.prevent="$store.state.isAdmin=!$store.state.isAdmin"
            class="
              btn btn-d btn-sm
              w-100
              d-flex
              align-items-center
              justify-content-center
              btn-success
            "
          >
            User
          </button>
        </div>
          
        <router-link to="/addProduct" class="text-decoration-none p-2">
          <button v-if="$store.state.isAdmin"
            class="
              btn btn-warning btn-sm
              w-100
              d-flex
              align-items-center
              justify-content-center
            "
          >
            Add Product
          </button>
        </router-link>
        <router-link to="/addCategory" class="text-decoration-none p-2">
          <button v-if="$store.state.isAdmin"
            class="
              btn btn-warning btn-sm
              w-100
              d-flex
              align-items-center
              justify-content-center
            "
          >
            Add Category
          </button>
        </router-link>
        <router-link to="/deleteCategory" class="text-decoration-none p-2">
          <button v-if="$store.state.isAdmin"
            class="
              btn btn-warning btn-sm
              w-100
              d-flex
              align-items-center
              justify-content-center
            "
          >
            Delete Category
          </button>
        </router-link>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      isAdmin: false,
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
header {
  background-color: #dabb42;
  h2 {
    text-shadow: -1px 3px 2px rgba(0, 0, 0, 0.3);
    &.cursor {
      cursor: pointer;
    }
  }
}
</style>