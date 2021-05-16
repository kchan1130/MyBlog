
<template>
  <div class="footer">
    <div>MyBlog ©2021 Created by kchan</div>
    <div class="number">
      <a href="http://www.beian.miit.gov.cn" target="_blank"
        >TODO 备案号</a
      >
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Footer",
});
</script>
<style scoped>
.footer {
  text-align: center;
  padding: 20px;
  font-weight: bold;
}
</style>

