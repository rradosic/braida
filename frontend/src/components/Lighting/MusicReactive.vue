<template>
  <div class="">
    <div class="field">
      <b-switch>{{ $t("lighting.music.autoanim") }}</b-switch>
    </div>
    <b-field :label="$t('common.animation')">
      <b-select placeholder="Select a type" required>
        <option value="music">Energy</option>
        <option value="static">VU Spectrum</option>
        <option value="festive">Scrolling</option>
      </b-select>
    </b-field>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>