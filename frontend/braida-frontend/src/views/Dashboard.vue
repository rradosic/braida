<template>
    <div id="dashboard" key="dashboard">
        <router-link to="/about">
            <div class="dashboard-card">
                <div class="card-img flex flex-center">
                    <img src="../assets/images/dashboard/lighting.svg" alt="">
                </div>
                <p class="card-bottom-text">Lighting</p>
            </div>
        </router-link>
        <router-link to="/music">
            <div class="dashboard-card">
                <div class="card-img flex flex-center">
                    <img src="../assets/images/dashboard/music.svg" alt="">
                </div>
                <p class="card-bottom-text">Music</p>
            </div>
        </router-link>
        <router-link to="/settings">
        <div class="dashboard-card">
            <div class="card-img flex flex-center">
                <img src="../assets/images/dashboard/settings.svg" alt="">
            </div>
            <p class="card-bottom-text">Settings</p>
        </div>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'Dashboard',
}
</script>

<style>

</style>