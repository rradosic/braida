<template>
  <div class="about submenu" key="settings">
    <h1 class="title">{{ $t("title.settings") }}</h1>

    <h2 class="subtitle is-6">Customize your system settings</h2>
    <section>
      <b-tabs >
        <b-tab-item :label="$t('common.general')">
          <general :options="saveData.general"></general>
        </b-tab-item>

        <b-tab-item :label="$t('common.ledSetup')">
          <led-setup :options="saveData.ledSetup"></led-setup>
        </b-tab-item>
      </b-tabs>
    </section>
    <div class="buttons mt-5">
      <b-button @click="saveFormData" type="is-primary" expanded>{{
        $t("common.apply")
      }}</b-button>
    </div>
  </div>
</template>

<script>
import General from "../components/Settings/General.vue";
import LedSetup from '../components/Settings/LedSetup.vue';
export default {
  components: { General, LedSetup},
  mounted()
    {
    var me = this;
    this.axios
      .get("/settings")
      .then((response) => (me.saveData = response.data));
  },
  data: () => {
    return {
      saveData: {
        general: {
          bluetoothName: "The Brajda",
        },
        ledSetup: {},
      },
    };
  },
  methods: {
    saveFormData() {
      var me = this;
      this.axios
        .post("/settings", this.saveData)
        .then((response) => {
          if(response.data.success){
            me.$emit('saveSuccess');
          }
        }).catch(() => me.$emit('saveError'));
    },
  },
};
</script>

<style>
</style>