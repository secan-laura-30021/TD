<template>
  <div class="password-change-done">
    <PasswordChangeDoneMessage main_message="Verifica-ti emailul!" info="Am trimis un email cu instructiuni pentru resetarea parolei!"></PasswordChangeDoneMessage>
  </div>
</template>

<script>
import PasswordChangeDoneMessage from "@/components/PasswordChangeDoneMessage";

export default {
  name: "EmailBoxCheckResetPassword",
  components: {PasswordChangeDoneMessage}
}
</script>

<style scoped>

</style>