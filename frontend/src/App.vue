<template>
  <div>
    <the-navbar />

    <div class="bg-blue-300">
      <waifu-cards-list :waifus="waifus" />
    </div>
  </div>
</template>

<script>
import { ref, onBeforeMount } from "vue";
import api from "./services/api";
import WaifuCardsList from "./components/WaifuCardsList.vue";
import TheNavbar from "./components/TheNavbar.vue";

export default {
  components: {
    TheNavbar,
    WaifuCardsList,
  },
  setup() {
    const waifus = ref([]);

    onBeforeMount(async () => {
      const { data: response } = await api.get("waifu/");

      waifus.value = response.data;
    });

    return {
      waifus,
    };
  },
};
</script>

<style>
</style>