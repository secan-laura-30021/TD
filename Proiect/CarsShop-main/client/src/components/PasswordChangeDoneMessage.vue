<template>
  <div class="password-change-done" align="center">
    <h1>{{ main_message }}</h1>
    <p>{{ info }}</p>
  </div>
</template>

<script>
export default {

  name: 'PasswordChangeDoneMessage',
  props: {
    main_message: String,
    info: String,
  }
}
</script>

<style scoped>

</style>