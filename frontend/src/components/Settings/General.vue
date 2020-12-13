<template>
  <section>
    <h1 class="title is-5">Connection</h1>
    <h2 class="subtitle is-6">{{ $t("settings.conn.desc") }}</h2>
    <b-field :label="$t('settings.bluetoothName')">
      <b-input v-model="options.bluetoothName"></b-input>
    </b-field>

    <b-field :label="$t('settings.wifiSSID')">
      <b-input v-model="options.wifiSSID"></b-input>
    </b-field>

    <b-field :label="$t('settings.wifiPassword')">
      <b-input
        v-model="options.wifiPassword"
        type="password"
        value="iwantmytreasure"
        password-reveal
      >
      </b-input>
    </b-field>

    <h1 class="title is-5 mt-5">Security</h1>
    <h2 class="subtitle is-6">{{ $t("settings.security.desc") }}</h2>

    <b-switch v-model="options.startupPassEnabled">{{
      $t("settings.startupPassEnabled")
    }}</b-switch>

    <b-field
      v-if="options.startupPassEnabled"
      :label="$t('settings.startupPass')"
    >
      <b-input
        v-model="options.startupPass"
        type="password"
        value="iwantmytreasure"
        password-reveal
      >
      </b-input>
    </b-field>
  </section>
</template>

<script>
export default {
  props: {
    options: Object,
  },
};
</script>

<style>
</style>