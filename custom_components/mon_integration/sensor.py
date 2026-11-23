"""Capteurs."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import MonConfigEntry
from .const import DOMAIN
from .coordinator import MonCoordinator


async def async_setup_entry(
    hass: HomeAssistant, entry: MonConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback
) -> None:
    async_add_entities([MonCapteur(entry.runtime_data)])


class MonCapteur(CoordinatorEntity[MonCoordinator], SensorEntity):
    """Exemple de capteur alimenté par le coordinateur."""

    _attr_has_entity_name = True
    _attr_translation_key = "value"

    def __init__(self, coordinator: MonCoordinator) -> None:
        super().__init__(coordinator)
        entry = coordinator.config_entry
        self._attr_unique_id = f"{entry.entry_id}_value"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)}, name="Mon intégration", entry_type=DeviceEntryType.SERVICE
        )

    @property
    def native_value(self):
        return self.coordinator.data.get("value")
