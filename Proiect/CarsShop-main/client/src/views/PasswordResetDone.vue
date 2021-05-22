<template>
  <div class="password-reset-done">
    <PasswordChangeDoneMessage main_message="Parola a fost resetata!" info="Parola ta a fost resetata. Ai grija sa nu uiti de ea data viitoare!"></PasswordChangeDoneMessage>
  </div>
</template>

<script>
import PasswordChangeDoneMessage from "@/components/PasswordChangeDoneMessage";
export default {
  name: "PasswordResetDone",
  components: {PasswordChangeDoneMessage}
}

</script>

<style scoped>

</style>