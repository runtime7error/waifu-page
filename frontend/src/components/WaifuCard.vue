<script>
export default {
  props: {
    waifu: Object,
  },
  setup(props) {
    return {
      ...props,
    };
  },
};
</script>

<template>
  <img
    class="
      w-full
      h-full
      object-cover
      rounded-lg
      shadow-xl
      transition
      duration-300
      transform
      hover:-translate-y-2
      hover:scale-105
      cursor-pointer
    "
    :src="waifu.imageUrl"
    :alt="waifu.alt"
  />
</template>