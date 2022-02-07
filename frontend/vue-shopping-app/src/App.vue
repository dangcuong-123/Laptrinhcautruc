<template>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  created(){
    this.$store.dispatch('getProductsAction'),
    this.$store.dispatch('getCategoriesAction')
  }
}
</script>

<style lang="scss">
</style>
