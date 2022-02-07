<template>
  <header class="py-3">
    <div class="container-md d-flex justify-content-between align-items-center">
      <h2 class="text-white">Vue Shopping</h2>
      <router-link to="/addProduct" class="text-decoration-none">
        <button
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
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {};
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