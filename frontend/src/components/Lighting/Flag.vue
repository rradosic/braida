<template>
  <div class="mt-5">
    <b-field label="Coutry">
      <b-select v-model="options.country" placeholder="Select a country">
                <option
                    v-for="option in data"
                    :value="option.id"
                    :key="option.id">
                    {{ option.name }}
                </option>
            </b-select>
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
      data: [
        {id:"hr", name:"Croatia"}
      ],
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