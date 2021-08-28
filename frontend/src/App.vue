<template>

<!-- navBar -->
<div>
  <div class="bg-blue-500">
    <nav class="flex items-center justify-between flex-wrap bg-teal-500 p-6">
      <div class="flex items-center flex-shrink-0 text-white mr-6">
        <span class="font-semibold text-xl tracking-tight">Waifu List</span>
      </div>
        <div class="block lg:hidden">
      </div>
        <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      </div>
    </nav>
  </div>

 
<!-- Waifu List -->
<div class="bg-blue-300">
  <waifu-cards-list :waifus="waifus"/>
</div>


</div>
</template>

<script>
import { ref, onBeforeMount } from 'vue'
import api from './services/api'
import WaifuCardsList from './components/WaifuCardsList.vue'

export default {
  components: {
    WaifuCardsList
  },
  setup() {
    const waifus = ref([])

    onBeforeMount(async() => {
      const { data: response } = await api.get('waifus/')

      waifus.value = response.data
    })

    return {
      waifus,
    }
  }
}
</script>

<style>

</style>