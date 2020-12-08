<template>
    <div>
        <label class="switch">
            <input :checked="checked" type="checkbox">
            <span class="slider round pull-right"></span>
        </label>
    </div>
</template>

<script>
export default {
    props: {
        checked: Boolean
    }
}
</script>

<style>

</style>