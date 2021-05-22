<template>
  <div class="footer-message" align="center">
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {

  name: 'FooterMessage',
  props: {
    message: String
  }
}
</script>

<style scoped>
.footer-message {
  background: #292b2c;
  color: #ffffff;
  padding: 2%;
}

.footer-message p {
  font-size: 18px;
}
</style>