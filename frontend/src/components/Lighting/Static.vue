<template>
  <div class="mt-5">
    <h1 class="title is-5">{{$t('lighting.static.name')}}</h1>
    <h2 class="subtitle is-6">{{$t('lighting.static.desc')}}</h2>
    <b-field :label="$t('common.color')">
      <v-swatches v-model="options.color" swatches="text-advanced"></v-swatches>
    </b-field>
  </div>
</template>

<script>
import VSwatches from "vue-swatches";
import "vue-swatches/dist/vue-swatches.css";

export default {
  components: { VSwatches },
  props: {
    options: Object,
  },
  data() {
    return {

    };
  },
  computed: {
  },
};
</script>

<style>
</style>