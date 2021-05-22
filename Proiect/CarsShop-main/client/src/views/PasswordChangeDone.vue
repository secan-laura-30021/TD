<template>
  <div class="password-change-done">
    <PasswordChangeDoneMessage main_message="Parola a fost schimbata!" info="Parola ta a fost schimbata. Ai grija sa nu uiti de ea data viitoare!"></PasswordChangeDoneMessage>
  </div>
</template>

<script>
import PasswordChangeDoneMessage from "@/components/PasswordChangeDoneMessage";
export default {
name: "PasswordChangeDone",
  components: {PasswordChangeDoneMessage}
}
</script>

<style scoped>

</style>