<template>
  <div class="mt-5">
    <h1 class="title is-5">Music reactive</h1>
    <h2 class="subtitle is-6">{{$t('lighting.music.desc')}}</h2>
    <div class="field">
      <b-switch v-model="options.autoanim">{{ $t("lighting.music.autoanim") }}</b-switch>
    </div>
    <b-field :label="$t('common.animation')">
      <b-select v-model="options.animation" placeholder="Select an animation" required>
        <option value="energy">Energy</option>
        <option value="vu">VU Spectrum</option>
        <option value="scroll">Scrolling</option>
      </b-select>
    </b-field>
  </div>
</template>

<script>
export default {
  props:{
    options: Object
  }
};
</script>

<style>
</style>