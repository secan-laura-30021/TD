<template>
  <div class="footer">
    <FooterMessage message="Copyright Laura Secan, All rights reserved;"></FooterMessage>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import FooterMessage from "@/components/FooterMessage";


export default {
  name: 'Footer',
  components: {
    HelloWorld,
    FooterMessage
  }
}
</script>

