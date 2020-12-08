<template>
    <router-link class="dashboard-link" :to="route">
        <div class="card dashboard-card">
            <div class="card-content mx-2 my-2">
                    <b-image class="has-ratio is-128x128 is-flex is-justify-content-center is-align-items-center"
                :src="image"
                alt="Lighting item"
            ></b-image>
            </div>
            <!-- <div class="card-content">
                <b-image
                :src="require('@/assets/images/dashboard/lighting.svg')"
                alt="Lighting item"
                ratio="601by235"
            ></b-image>
            </div> -->
            <footer class="card-footer">
                <p class="mx-2 my-2 has-text-weight-semibold is-size-5">
                    {{ title }}
                </p>
                
            </footer>
        </div>
    </router-link>
</template>

<script>
export default {
    props: {
        route: String,
        image: String,
        title: String,
    }
}
</script>

<style lang="scss">
.dashboard-card{
    max-width: 350px;
    width: 350px;
    >.card-content{
        padding: 0;
    }
    figure{
        margin: auto;
    }
}
</style>