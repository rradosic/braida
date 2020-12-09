<template>
  <div class="mt-5">
    <b-field label="Find a name">
      <b-autocomplete
        v-model="options.country"
        placeholder="Croatia"
        :open-on-focus="true"
        :data="filteredDataArray"
      >
      </b-autocomplete>
    </b-field>
  </div>
</template>

<script>
export default {
  props: {
    options: Object,
  },
  data() {
    return {
      data: ["Croatia", "England"],
      name: "",
      selected: null,
    };
  },
  computed: {
    filteredDataArray() {
      return this.data.filter((option) => {
        return (
          option.toString().toLowerCase().indexOf(this.name.toLowerCase()) >= 0
        );
      });
    },
  },
};
</script>

<style>
</style>