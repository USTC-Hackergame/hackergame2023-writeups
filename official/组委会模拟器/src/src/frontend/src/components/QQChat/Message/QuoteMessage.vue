<template>
  <div class="fakeqq-message__quote">
    <div class="fakeqq-message__quote-name">{{ name }}{{ time ? '&nbsp;' + time : '' }}</div>
    <div class="fakeqq-message__quote-content"><slot></slot></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'QuoteMessage',
  props: {
    name: { type: String, required: true },
    time: {
      type: String,
      default: '',
    },
  },
})
</script>
