<script>
import WaifuCard from "./WaifuCard.vue";

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
    };
  },
};
</script>

<template>
  <section
    class="
      min-h-[calc(100vh-4rem)]
      py-8
      px-4
      lg:px-0
      mx-auto
      w-full
      max-w-screen-lg
    "
  >
    <div class="grid grid-cols-3 gap-4">
      <waifu-card v-for="waifu in waifus" :waifu="waifu" :key="waifu.id" />
    </div>
  </section>
</template>
