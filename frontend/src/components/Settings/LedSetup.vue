<template>
  <section>
    <b-field :label="$t('settings.numberOfLeds')">
      <b-numberinput min='0' v-model="options.ledsNumber"></b-numberinput>
    </b-field>
  </section>
</template>

<script>
export default {
props:{
  options: Object
}
}
</script>

<style>

</style>