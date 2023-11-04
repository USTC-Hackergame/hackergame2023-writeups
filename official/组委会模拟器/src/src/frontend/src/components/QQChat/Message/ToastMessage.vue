<template>
  <div class="fakeqq-message fakeqq-toast"><slot></slot></div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ToastMessage',
})
</script>
