const getLocalValue = (itemName) => {
    const storageItem = localStorage.getItem(itemName)
    return storageItem ? JSON.parse(storageItem) : {}
}

const setLocalValue = (itemName, key, value) => {
    const obj = { [key]: value };
    const storageItem = getLocalValue(itemName);
    const storageItemValue = storageItem ? { ...storageItem, ...obj } : obj;
    localStorage.setItem(itemName, JSON.stringify(storageItemValue));
}

const incLocalValue = (itemName, key, value = 1) => {
    const storageItem = getLocalValue(itemName)
    const storageItemValue = storageItem[key] ? storageItem[key] : 0
    setLocalValue(itemName, key, storageItemValue + value)
}

const decLocalValue = (itemName, key, value = 1) => {
    const storageItem = getLocalValue(itemName)
    const storageItemValue = storageItem[key] ? storageItem[key] : 0
    setLocalValue(itemName, key, storageItemValue - value)
}