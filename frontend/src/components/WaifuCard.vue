<script>
export default {
  props: {
    waifu: Object,
  },
  setup(props) {
    return {
      ...props,
    }
  } 
}
</script>

<template>
  <img class="w-full h-full object-cover" :src="waifu.imageUrl" :alt="waifu.alt" />
</template>