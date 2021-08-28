<script>
import WaifuCard from './WaifuCard.vue'

export default {
  props: {
    waifus: Array,
  },
  components: {
    WaifuCard,
  },
  setup(props) {
    return {
      ...props,
    }
  }
}
</script>

<template>
  <div class="grid grid-cols-3 gap-3 p-3">
    <waifu-card v-for="waifu in waifus" :waifu="waifu" :key="waifu.id" />
  </div>
</template>
