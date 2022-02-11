export default function cleanSet(set, startString) {
  if (startString && typeof startString === 'string') {
    const nstrings = [];
    for (const item of set) {
      if (item.startsWith(startString)) {
        nstrings.push(item.slice(startString.length));
      }
    }
    return nstrings.join('-');
  }
  return '';
}
