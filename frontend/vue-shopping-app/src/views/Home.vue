<template>
  <div>
    <Header />
    <Products />
  </div>
</template>

<script>
import Header from "../components/Header.vue";
import Products from "../components/Products.vue";

export default {
  name: "Home",
  components: { Header, Products },
};
</script>

    